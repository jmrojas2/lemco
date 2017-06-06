from dashboard.models import work_file
from table import Table
from table.utils import A
from table.columns import Column, LinkColumn, Link

class ArchivoTable(Table):
	number = Column(field='number', header=u'Numero de Archivo')
	status = Column(field='status', header=u'Estado')
	actual_time = Column(field='actual_time', header=u'Tiempo en Proceso')
	total_time = Column(field='accumulated_time', header=u'Tiempo Total')
	ver = LinkColumn(header=u'Detalles', links=[Link(text=u'Ver', viewname='dashboard_file_check2', args=(A('number'),))], sortable=False)
