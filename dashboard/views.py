from django.shortcuts import render
from dashboard.tables import ArchivoTable
from dashboard.models import work_file
from .forms import checkNumber
from django.utils.timezone import utc
import datetime
process = 2
area = '-'

def files_list(request):
	form = checkNumber()
	now = datetime.datetime.utcnow().replace(tzinfo=utc)
	for archivo in work_file.objects.filter(actual_process=process):
		if archivo.status == 'iniciado':
			timediff = now - archivo.ini_date_process
			archivo.actual_time = timediff
			archivo.save()
		else:
			if archivo.actual_process != 1:
				timediff2 = now - archivo.finish_date_process
				archivo.actual_time = timediff2
			else:
				archivo.actual_time = '-'
			archivo.save()
		timediff_total = now - archivo.ini_date
		archivo.accumulated_time = timediff_total
		archivo.save()
	if process == 2:
		archivos = ArchivoTable(work_file.objects.filter(actual_process=process))
	else:
		archivos = ArchivoTable(work_file.objects.filter(actual_process=process))
	
	
	if request.method == "POST":
		number = request.POST['numero']
		file_check = work_file.objects.get(number=number)
		time_diffe = now - file_check.ini_date_process
		if file_check.actual_process == process:
			if file_check.status == 'pendiente':
				file_check.status = 'iniciado'
				if process == 1:				
					file_check.status_one = 'iniciado'
					file_check.ini_date_process1 = now
				if process == 2:
					file_check.status_two = 'iniciado'
					file_check.ini_date_process2 = now
				if process == 3:
					file_check.status_three = 'iniciado'
					file_check.ini_date_process3 = now
				if process == 4:
					file_check.status_four = 'iniciado'
					file_check.ini_date_process4 = now
				file_check.ini_date_process = datetime.datetime.utcnow().replace(tzinfo=utc)
				file_check.save()

				return render(request, 'lista.html', {'archivos':archivos, 'form':form, 'process':process, 'area':area})
			if file_check.status == 'iniciado':
				file_check.actual_process = process + 1
				file_check.status = 'pendiente'

				if process == 1 and file_check.status_one != 'terminado':				
					file_check.time_process1 = time_diffe
					file_check.status_one = 'terminado'
					file_check.finish_date_process1 = now
				if process == 2 and file_check.status_two != 'terminado':
					file_check.time_process2 = time_diffe
					file_check.status_two = 'terminado'
					file_check.finish_date_process2 = now
				if process == 3 and file_check.status_three != 'terminado':
					file_check.time_process3 = time_diffe
					file_check.status_three = 'terminado'
					file_check.finish_date_process3 = now
				if process == 4 and file_check.status_four != 'terminado':
					file_check.time_process4 = time_diffe
					file_check.status_four = 'terminado'
					file_check.finish_date_process4 = now
				file_check.finish_date_process = now
				file_check.save()	
				return render(request, 'lista.html', {'archivos':archivos, 'form':form, 'process':process, 'area':area})
	
	return render(request, 'lista.html', {'archivos':archivos, 'form':form, 'process':process, 'area':area})
	
def file_check(request):
	
	form = checkNumber()
	now = datetime.datetime.utcnow().replace(tzinfo=utc)
	if request.method == "POST":
		number = request.POST['numero']
		file_check = work_file.objects.get(number=number)
		time_diffe = now - file_check.ini_date_process
		time_diffe2 = now - file_check.finish_date_process
		file_check.actual_time = time_diffe
		if file_check.status == 'iniciado':
			if file_check.actual_process == 1:				
				file_check.time_process1 = time_diffe
			if file_check.actual_process == 2:
				file_check.time_process2 = time_diffe
			if file_check.actual_process == 3:
				file_check.time_process3 = time_diffe
			if file_check.actual_process == 4:
				file_check.time_process4 = time_diffe
		if file_check.status == 'pendiente':
			if file_check.actual_process == 1:				
				file_check.time_process1 = time_diffe2
			if file_check.actual_process == 2:
				file_check.time_process2 = time_diffe2
			if file_check.actual_process == 3:
				file_check.time_process3 = time_diffe2
			if file_check.actual_process == 4:
				file_check.time_process4 = time_diffe2
		file_check.save()
		return render(request, 'check_list.html', {'form':form, 'file_check':file_check})
	
	return render(request, 'check_list.html', {'form':form})
	
def file_check2(request, number):
	file_check = work_file.objects.get(number=number)
	now = datetime.datetime.utcnow().replace(tzinfo=utc)
	time_diffe = now - file_check.ini_date_process
	time_diffe2 = now - file_check.finish_date_process
	form = checkNumber()
	if file_check.status == 'iniciado':
		if file_check.actual_process == 1:				
			file_check.time_process1 = time_diffe
		if file_check.actual_process == 2:
			file_check.time_process2 = time_diffe
		if file_check.actual_process == 3:
			file_check.time_process3 = time_diffe
		if file_check.actual_process == 4:
			file_check.time_process4 = time_diffe
	if file_check.status == 'pendiente':
		if file_check.actual_process == 1:				
			file_check.time_process1 = time_diffe2
		if file_check.actual_process == 2:
			file_check.time_process2 = time_diffe2
		if file_check.actual_process == 3:
			file_check.time_process3 = time_diffe2
		if file_check.actual_process == 4:
			file_check.time_process4 = time_diffe2	
	file_check.save()
	return render(request, 'check_list.html', {'form':form, 'file_check':file_check})
	
def file_filter(request):
	
	now = datetime.datetime.utcnow().replace(tzinfo=utc)
	if request.method == "POST":
		actual_process = request.POST['process']
		
		
		for archivo in work_file.objects.filter(actual_process=actual_process):
			if archivo.status == 'iniciado':
				timediff = now - archivo.ini_date_process
				archivo.actual_time = timediff
				archivo.save()

				
			else:
				archivo.actual_time = '-'
				archivo.save()
			timediff_total = now - archivo.ini_date
			archivo.accumulated_time = timediff_total
			archivo.save()
		
		
		
		archivos = ArchivoTable(work_file.objects.filter(actual_process=actual_process))
		
		return render(request, 'filtro.html', {'archivos':archivos, 'actual_process':actual_process})
	return render(request, 'filtro.html')

	
