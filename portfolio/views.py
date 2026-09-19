from pathlib import Path
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def download_cv(request):
    cv_path = Path(settings.BASE_DIR) / "static" / "docs" / "yehiasalah.pdf"
    if not cv_path.exists():
        raise Http404("CV not found")
    response = FileResponse(open(cv_path, "rb"), content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="Yehia_Salah_CV.pdf"'
    return response
