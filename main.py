# Lesson_Cod
# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def docPrinter(self):
#         print(f" сформирован отчёт {self.title} - {self.content}")

from abc import ABC, abstractmethod

class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass

class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)

class HtmlFormatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")

class Report():
    def __init__(self, title, content, formated):
        self.title = title
        self.content = content
        self.formated = formated

    def docPrinter(self):
        self.formated.format(self)

report = Report("заголовок отчета", "это основной текст - его тут много", HtmlFormatted())

report.docPrinter()
