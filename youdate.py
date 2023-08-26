from flet import *
from datepicker.datepicker import DatePicker
from datepicker.selection_type import SelectionType
from datetime import datetime


class Youdate(UserControl):
	def __init__(self):
		super().__init__()
		self.datepicker =  None
		self.holidays = [datetime(2023,4,25),datetime(2023,5,1),datetime(2023,6,2)]
		self.locales = ["en_US"]	
		self.selected_locale = None

		# AND HERE FOR RESULT YOU SELECTED
		self.you_select_date = Text(size=30,weight="bold")

		self.locales_opts = []

		for l in self.locales:
			self.locales_opts.append(
				dropdown.Option(l)
				)
		# AND NOW I WILL MAKE DIALOG FOR INPUT DATE
		self.dlg_modal = AlertDialog(
			modal=True,
			title=Text("Select date here"),
			actions=[
				TextButton("Cancel",
					on_click=self.cancel_dlg
					),
				TextButton("Confirm",
					on_click=self.confirm_dlg
					),
			],
			actions_alignment="end",
			actions_padding=5,
			content_padding=0
			)

		# AND NOW I WIL MAKE TEXTFIELD 
		self.tf = TextField(
			label="select here",
			dense=True,
			width=260,height=50
			)
		# AND I WILL MAKE ICON DATE INSIDE TEXTFIELD
		self.cal_icon = TextButton(
			icon=icons.CALENDAR_MONTH,
			on_click=self.open_dlg_modal,
			height=40,
			width=40,
			right=0,
			style=ButtonStyle(
				padding=Padding(4,0,0,0),
				shape={
					MaterialState.DEFAULT:RoundedRectangleBorder(radius=1)
				}

				)
			)
		# AND I WILL ADD STACK TEXTFIELD AND ICON CALENDATA
		self.st = Stack([
			# YOU TEXTFIELD HERE
			self.tf,
			# AND ICON CALENDAR HERE
			self.cal_icon
			])
		self.from_to_text = Text(visible=False)



	def build(self):
		return Column([
			Text("test date",size=30,weight="bold"),

			# SHOW YOU TEXTFIELD
			self.st,
			self.from_to_text,
			self.you_select_date
			])
	# AND NOW I WILL ADD EACH FUNCTION FOR OPEN AND CLOSE
	# DIALOG
	def confirm_dlg(self,e):
		selected_date = self.datepicker.selected_data[0] if len(self.datepicker.selected_data) > 0 else None
		# AND NOW I WILL CONVERT TO FORMAT DD/MM/YYYY
		selected_data_str = selected_date.strftime("%Y-%m-%dT%H:%M:%S") if selected_date else None
		formated_date = self._format_date(selected_data_str)
		self.tf.value = formated_date
		# AND YOU CAN SEE RESULT IN TERMINAL
		print("you date",self.tf.value)

		# AND SHOW RESULT IN SCREEN
		self.you_select_date.value = self.tf.value

		# AND CLOSE DIALOG
		self.dlg_modal.open = False
		self.update()
		self.page.update()

	# AND IF YOU CLICK CANCEL BUTTON IN DIALOG
	def cancel_dlg(self,e):
		self.dlg_modal.open = False
		self.page.update()

	# AND IF YOU CLICK AND SHOW DIALOG OPEN
	def open_dlg_modal(self,e):
		self.datepicker = DatePicker(
			# YOU CAN SHOW HOUR OR MINUTE 
			hour_minute=True,
			selected_date=None,
			# AND THIS CODE FOR SINGLE INPUT
			# YOU CAN ADD 0 . AND FOR Multilple
			# YOU CAN ADD 1 for date range picker
			# AND FOR MULTIPLE INPUT DATE YOU CAN 
			# add value is 2,
			# NOW I SHOW YOU FOR SINGLE DATE INPUT
			# THEN I USE 0
			selection_type=int(0),
			# AND FOR SATURDAY AND SUNDAY
			holidays=self.holidays,
			# AND YOU CAN SHOW 3 MONTH IN DATE PICKER
			# YOU CAN SET LIKE THIS
			show_three_months=False,
			locale=self.selected_locale
			)
		self.page.dialog = self.dlg_modal
		self.dlg_modal.content = self.datepicker
		self.dlg_modal.open = True
		self.page.update()

	# AND NOW I WILL MAKE FUNCTION FOR FORMATED DATE
	# TO mm/dd/yyyy
	def _format_date(self,date_str):
		if date_str:
			date_obj = datetime.strptime(date_str,"%Y-%m-%dT%H:%M:%S")
			formated_date = date_obj.strftime("%d %B %Y")
			return formated_date
		else:
			return ""


