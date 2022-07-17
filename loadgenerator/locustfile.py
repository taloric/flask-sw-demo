from locust import HttpUser, TaskSet, between


def fulltest(l):
    l.client.get("http://python-micro-ui:5000/app/testall")


class UserBehavior(TaskSet):

    tasks = {fulltest: 10}


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 10)

# test :
# locust --host="http://${HOST}" --headless -u "{USERS}"
