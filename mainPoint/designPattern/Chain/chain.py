#!/usr/bin/python
#coding=utf-8

# 责任链模式用于实现软件中的松散耦合，其中来自客户端的指定请求通过包含在其中的对象链传递。 它有助于构建一系列对象。 请求从一端进入并从一个对象移动到另一个对象。该模式允许对象发送命令而不知道哪个对象将处理该请求。

class ReportFormat(object):
	PDF = 0
	TEXT = 1
	PHP = 2
	
class Report(object):
	def __init__(self, format_):
		self.title = 'Monthly report'
		self.text = ['Things are going', 'really, really well.']
		self.format_ = format_
		
class Handler(object):
	def __init__(self):
		self.nextHandler = None
		
	def handle(self, request):
		self.nextHandler.handle(request)
		
class PDFHandler(Handler):
	def handle(self, request):
		if request.format_ == ReportFormat.PDF:
			self.output_report(request.title, request.text)
		else:
			super(PDFHandler, self).handle(request)
			
	def output_report(self, title, text):
		print '<html>'
		print '<head>'
		print '<title>%s</title>' % title
		print '</head>'
		print '<body>'
		for line in text:
			print '<p>%s</p>' % line
		print '</body>'
		print '</html>'
		
class TextHandler(Handler):
	def handle(self, request):
		if request.format_ == ReportFormat.TEXT:
			self.output_report(request.title, request.text)
		else:
			super(TextHandler, self).handle(request)
			
	def output_report(self, title, text):
		print 5 * '*' + ' ' + title + ' ' + 5 * '*'
		for line in text:
			print line
			
class ErrorHandler(Handler):
	def handle(self, request):
		print 'Invalid request'
		
if __name__ == "__main__":
	report = Report(ReportFormat.TEXT)
	pdf_handler = PDFHandler()
	text_handler = TextHandler()
	
	pdf_handler.nextHandler = text_handler
	text_handler.nextHandler = ErrorHandler()
	pdf_handler.handle(report)

		
	
