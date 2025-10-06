from django.shortcuts import render
import google.generativeai as genai
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# ✅ Load API key
genai.configure(api_key=settings.GEMINI_API_KEY)

# ✅ Setup Gemini model
model = genai.GenerativeModel(
    "models/gemini-2.5-flash",
    system_instruction=(
        "You are an AI assistant created by Muhammad Rehan. "
        "If anyone asks 'Who created you?' or 'Who made you?', "
        "you must respond with the name Muhammad Rehan. "
        "All your responses must be in clean HTML format, without code fences or markdown.","you should also add some design to your response using inline css ","if there is any code snippet in the response there should be button to copy that code and it should be  just after the code snippet","Promote only good thing Don't reply to question that include 18+ activities ","Reply in same tone as the user uses","Mostly stay polite"
    )
)

@csrf_exempt
def chat_view(request):
    response_text = None  # Default

    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            response = model.generate_content(prompt)
            raw_response = response.text

            # ✅ Remove ```html and ``` wrappers if present
            if raw_response.startswith("```"):
                raw_response = (
                    raw_response
                    .replace("```html", "")
                    .replace("```", "")
                    .strip()
                )

            response_text = raw_response

    return render(request, "chat_messages.html", {"response": response_text})