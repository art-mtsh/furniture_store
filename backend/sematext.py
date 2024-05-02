import logging.handlers

handler = logging.handlers.SysLogHandler(address=('logsene-syslog-receiver.eu.sematext.com', 514))

formater = logging.Formatter("886c2329-fe6c-4529-a321-e65c6742dd94:%(message)s")
handler.setFormatter(formater)

logger = logging.getLogger("HelloLogs")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# logger.info("Info")
log_engine = logger

