from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from app import App
import sys

class AppContext(ApplicationContext):
	def run(self):
		window = App()
		return self.app.exec_()


def main():
	appctxt = AppContext()
	try:
		sys.exit(appctxt.run())
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()
	