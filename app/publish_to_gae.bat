@echo ################################
@echo ################################
@echo ####### Are you Sure empeericpaypal? #########
@echo ################################
@echo ################################
@pause
python "c:\Program Files\Google\google_appengine\appcfg.py" --application=empeericpaypal --no_cookies -v -V 1 update .
@pause