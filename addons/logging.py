#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging, traceback
logger = logging.getLogger('delegito')
logger.setLevel(logging.WARNING)
logging.debug('Loaded API')
if __name__ == '__main__':
	logging.getLogger('stem').setLevel(logging.WARNING)
	logging.getLogger('flask').setLevel(logging.INFO)
	logging.basicConfig(level=logging.DEBUG)
	logger = logging.getLogger(__name__)
	logging.info('Welcome to Komento')
	try:
		# torp = start_tor()
		# controller = start_controller()
		# offered_rendesvous = offer_rendesvous(controller)
		# logging.info("Access rendesvous on: http://%s.onion" % offered_rendesvous)
		app.run(host="0.0.0.0",port=5000,debug=True)
	except:
		logging.critical(traceback.format_exc())
	finally:
		logging.info("Komento - shutdown.")
		try:
			# controller.from_port().remove_ephemeral_hidden_service(offered_rendesvous)
			# controller.close()
			# stop_tor(torp)
			logging.debug("rendesvous deleted successfully")
		except:
			pass
