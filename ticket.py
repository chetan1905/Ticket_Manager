# This class is responsible for defining and creating a ticket object
from utils import Ticket_Status
from datetime import datetime as dt

class Ticket:
    def __init__(self, ticket_number: str, ticket_url: str, ticket_status: Ticket_Status, start_date_time: str, end_date_time: str | None, ticket_points: int | None):
        self.ticket = ticket_number
        self.url = ticket_url
        self.status = ticket_status
        self.start = start_date_time
        self.end = end_date_time
        self.points = ticket_points

    @staticmethod
    def create_ticket():
        number = input("Enter your ticket number: ")
        url = input("Enter your ticket url: ")
        status = input("Enter your ticket status (IP/CR/IT/D): ")
        points = input("Enter the points assigned to your ticket: ")