class Solution:
    def smallestChair(self, times, targetFriend):
        events = []  # to store both arrival and leave events

        # populate events with arrival and leave times
        for i in range(len(times)):
            events.append([times[i][0], i])  # Arrival
            events.append([times[i][1], ~i])  # Leave

        events.sort()  # Sort events by time

        available_chairs = list(
            range(len(times))
        )  # Tracking chairs that are free

        occupied_chairs = []  # When each chair will be free

        for event in events:
            time, friend = event

            # free up chairs if friends leave
            while occupied_chairs and occupied_chairs[0][0] <= time:
                _, chair = heapq.heappop(
                    occupied_chairs
                )  # Pop chair that becomes empty
                heapq.heappush(available_chairs, chair)  # available chairs

            # If friend arrives
            if friend >= 0:
                chair = heapq.heappop(available_chairs)
                if friend == targetFriend:
                    return chair
                heapq.heappush(
                    occupied_chairs, [times[friend][1], chair]
                )  # chair will be occupied till this time

        return -1  # should not come to this point