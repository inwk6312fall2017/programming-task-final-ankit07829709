import create_ticket as ticketgen
import requests

 def ticketcount():

  ticket = ticketgen.get_ticket()
  api = "/api/v1/network-device/count"
  controller = 'sandboxapic.cisco.com'
  api = "/api2/v2/network-device/count"
  url = "https://" + controller + api
