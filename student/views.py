from django.shortcuts import render
from student.models import Student
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def insert(request):
   if request.POST:
      post = request.POST
      new_student = Student(
         num = post["num"],
         name = post["name"],
         chinese = post["chinese"],
         math = post["math"],
         english = post["english"],
         physics = post["physics"],
         chemistry = post["chemistry"],
         allscore = int(post["chinese"])+int(post["math"])+int(post["english"])+int(post["physics"])+int(post["chemistry"]))
      new_student.save()
   return render(request, 'insert.html')


def list(request):
    student_list = Student.objects.all()
    c = {"student_list": student_list, }
    return render(request, "list.html", c)


def list2(request):
   student_list = Student.objects.all()
   c = {"student_list": student_list, }
   return render(request, "list2.html", c)


def delete(request):
   delete_num = request.GET.get('delete_num')
   Student.objects.get(num = delete_num).delete()
   return render(request, "delete.html")


def updateStudent(request):
   update_num = request.GET.get('update_num')
   update_student = Student.objects.get(num=update_num)
   a = {"update_student": update_student, }
   if request.POST:
      update_name = request.POST.get("name")
      update_chinese = request.POST.get("chinese")
      update_math = request.POST.get("math")
      update_english = request.POST.get("english")
      update_physics = request.POST.get("physics")
      update_chemistry = request.POST.get("chemistry")

      update_student.num = update_num
      update_student.name = update_name
      update_student.chinese = update_chinese
      update_student.math = update_math
      update_student.english = update_english
      update_student.physics = update_physics
      update_student.chemistry = update_chemistry
      update_student.allscore =int(update_chemistry)+int(update_physics)+int(update_english)+int(update_math)+int(update_chinese)
      update_student.save()
   return render(request, "update.html", a)

