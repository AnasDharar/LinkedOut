from django.http import JsonResponse
from django.shortcuts import render
from pyscripts.scraper import scrape_data
from pyscripts.summarizer import summarize_text

def index(request):
    return render(request, "summarizer/index.html")

def summarize_post(request):
    if request.method == "POST":
        url = request.POST.get("url")
        if not url:
            return JsonResponse({"error": "No URL provided."}, status=400)
        data = scrape_data(url)
        summary = summarize_text(data)
        return JsonResponse({
            "url": url,
            "author": data[0],
            "text": data[1],
            "summary": summary
        })
    return JsonResponse({"error": "Invalid request."}, status=400)
