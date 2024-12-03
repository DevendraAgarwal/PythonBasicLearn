class Proxy:
    def __init__(self, subject):
        self.subject = subject

    def request(self):
        if self.subject.is_available:
            self.subject.use()
        else:
            print("Proxy: Subject unavailable")

class RealSubject:
    def __init__(self):
        self.is_available = True

    def use(self):
        print("Real Subject: Using")

# Usage:
subject = RealSubject()
proxy = Proxy(subject)

proxy.request()  # Output: Real Subject: Using