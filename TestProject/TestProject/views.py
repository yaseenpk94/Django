from django.shortcuts import render


def index(request):
    return render(request, "Index.html")


def calculator(request):
    val1 = int(request.GET.get('num1'))
    val2 = int(request.GET.get('num2'))
    operator = request.GET.get('operator')
    answer = None

    if operator == "+":
        answer = val1 + val2
    elif operator == "-":
        answer = val1 - val2
    elif operator == "*":
        answer = val1 * val2
    elif operator == "/":
        answer = val1 / val2
    else:
        answer = "Some thing went wrong."

    print(answer)

    
    result = {"answer": answer}

    return render(request, "calculator.html", result)