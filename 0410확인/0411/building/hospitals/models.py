from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name} 전문의'
    
class Patient(models.Model):
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) 외래키 삭제
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
    
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    # 아래와 같은 정보들을 저장하기 위해선 중개 테이블을 직접 만들어야 함
    symptom = models.TextField()
    reserved_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'