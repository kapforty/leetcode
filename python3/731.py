class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # check for triple booking
        for s, e in self.overlaps:
            if max(start, s) < min(end, e): return False

        # update overlaps
        for s, e in self.bookings:
            if max(start, s) < min(end, e):
                self.overlaps.append([max(start, s), min(end, e)])
        self.bookings.append([start, end])
        return True
