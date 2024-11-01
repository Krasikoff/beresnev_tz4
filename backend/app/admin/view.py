from sqladmin import ModelView
from app.models.user import User
# from app.models.reservation import Reservation
# from app.models.meeting_room import MeetingRoom
# from app.models.file import File


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]
    column_details_exclude_list = [User.hashed_password]
    can_delete = False
    icon = 'fa-solid fa-user'


# class ReservationAdmin(ModelView, model=Reservation):
#     column_list = [
#         c.name for c in Reservation.__table__.c] + [
#             Reservation.user] + [Reservation.meetingroom]
#     icon = 'fa-solid fa-bed'


# class MeetingRoomAdmin(ModelView, model=MeetingRoom):
#     column_list = [
#         c.name for c in MeetingRoom.__table__.c] + [MeetingRoom.reservation]
#     icon = 'fa-solid fa-book'


# class FileAdmin(ModelView, model=File):
#     column_list = [File.id, File.file]
#     icon = 'fa fa-file'
