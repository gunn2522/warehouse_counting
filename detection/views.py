from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse
from .models import Product, FlowLog
from .yolo_handler import update_inventory
from ultralytics import YOLO
import cv2
import pandas as pd

model = YOLO("yolov8n.pt")

def index(request):
    return render(request, 'dashboard.html')

def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)
        labels = results[0].names
        class_ids = results[0].boxes.cls.cpu().numpy().astype(int)

        for cls in class_ids:
            label = labels[cls]
            stock = update_inventory(label, 'IN')

            product, _ = Product.objects.get_or_create(name=label, defaults={"category": "General"})
            product.stock = stock
            product.save()

            FlowLog.objects.create(product=product, action='IN', quantity=1)

        annotated = results[0].plot()
        ret, buffer = cv2.imencode('.jpg', annotated)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def detection_log(request):
    logs = FlowLog.objects.all().order_by('-timestamp')
    return render(request, 'detection_log.html', {'logs': logs})

def end_of_day_report(request):
    logs = FlowLog.objects.all().order_by('-timestamp')
    df = pd.DataFrame(list(logs.values('product__name', 'action', 'quantity', 'timestamp')))
    inflow = df[df['action'] == 'IN'].groupby('product__name')['quantity'].sum()
    outflow = df[df['action'] == 'OUT'].groupby('product__name')['quantity'].sum()
    summary = inflow.subtract(outflow, fill_value=0)
    return render(request, 'report.html', {'stock_summary': summary.to_dict()})

def download_report_excel(request):
    logs = FlowLog.objects.all().values('product__name', 'action', 'quantity', 'timestamp')
    df = pd.DataFrame(logs)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="inventory_report.xlsx"'
    df.to_excel(response, index=False)
    return response
