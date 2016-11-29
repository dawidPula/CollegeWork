import random
import time
import threading

class Queue:

    def __init__(self):
    #creates a queue implemented in a list
    #queue will implement distribution of the messages to the servers
        self._queue = []
        self._size= 0
        self._lock = False
        self._servers = {}
        self._clients = {}

    def insert(self,item):
    #adds an item to the end of the queue
        self.lock()
        self._queue.append(item)
        self._size += 1
        self.unlock()

    def pop(self):
    #returns and removes the item at the front of the queue
        self._size -= 1
        return self._queue.pop(0)

    def size(self):
    #returns size of queue
        return self._size

    def isEmpty(self):
    #returns True if queue is empty else false
        return self._size == 0

    def isLocked(self):
        #returns the status of the lock currently on the queue
        return self._lock

    def lock(self):
        #locks the queue for mutex
        self._lock = True

    def unlock(self):
        #unlocks the queue for mutex
        self._lock = False

    def registerServer(self,serverId,server):
        #registers a server with the message queue
        self._servers[serverId] = server

    def registerClient(self,clientId,client):
        #registers a new client to recive messages
        self._clients[clientId] = client  

    def getMessage(self,serverid):
        #returns the next available job to the awaiting server.
        #if there is no jobs available will return False stopping the server server
        for message in range(len(self._queue)):
            if self._queue[message].reciver() == serverid:
                return self._queue.pop(message)
        return False
        #    if message.reciver() in self._servers and self._servers[message.reciver()].busy():
        #        return self._servers[message.reciver()].work(message)


    def reply(self,clientId,messageId,result):
        #sends a reply to the appropriate client
        self._clients[clientId].reciveMessage(messageId,result)
        
class Message:
    _Id = 0
    def __init__(self,client,server,func):
        #class to make threads do work
        self._id = Message._Id
        Message._Id += 1
        self._sender = client
        self._reciver = server
        self._time = random.randrange(1,4)
        self._func = func
    
    def __str__(self):
        return "id:%i func:%s"%(self._id,self._func)
    
    def work(self):
        #waits then does a simple maths equation
        time.sleep(self._time)
        return(int(eval(self._func)))
    
    def getId(self):
        return self._id

    def reciver(self):
        return self._reciver

    def sender(self):
        return self._sender

class Server(threading.Thread):
    def __init__(self,serverId,queue):
        #Implements a thread acessing the queue 
        threading.Thread.__init__(self)
        self._serverId = serverId
        self._message = None
        self._queue = queue
        print("starting server:%s\n"%(self._serverId))

    def run(self):
        #when the thread is ready it takes a message from the queue if
        #the queue is not empty and not locked by another thread
        working = True
        time.sleep(5)
        while working:
            if not self._queue.isLocked():
                self._queue.lock()
                self._message = self._queue.getMessage(self._serverId)
                self._queue.unlock()
                if self._message == False :
                    working = False
                    break
                messageid, result = self._message.getId(), self._message.work()
                print("server:%s working on message : %i\n"%(self._serverId,messageid))
                self._queue.reply(self._message.sender(),messageid,result)
        print("exiting server:%s\n"%(self._serverId))

class Client(threading.Thread):
    #client class will create a number of messages and add the to the queue
    #then it will wait for the messages to return to it and print out the result

    _id = 0
    def __init__ (self,queue):
        threading.Thread.__init__(self)
        self._id = Client._id
        Client._id += 1
        self._messageId = set()
        self._messages =[]
        self._queue = queue

    def createMessage(self):
        task = random.choice(["-","+","*","/"])
        func = "%i %s %i" %(random.randrange(1,10),task,random.randrange(1,10))
        message = Message(self._id,task,func)
        self._messages.append(message)
        self._messageId.add(message.getId())

    def reciveMessage(self,id,result):
        print("Message ID:%i Result:%i\n" %(id,result))
        self._messageId.remove(id)

    def getId(self):
        return self._id


    def run(self):
        for _ in range(random.randrange(2,6)):
            self.createMessage()
        print("client: %i created:%i messages\n" %(self._id,len(self._messageId)))
        while len(self._messages) != 0:
            if not self._queue.isLocked():
                self._queue.insert(self._messages.pop(0))
        while len(self._messageId) > 0:
            pass
        print("all messages recived exiting client:%i\n" %(self._id))
        


def main():
    q = Queue()
    c =[] 
    for _ in range(3):
        c.append(Client(q))
    for client in c:
        q.registerClient(client.getId(),client)

    s= []
    for sid in ["/","*","-","+"]:
        server = Server(sid,q)
        s.append(server)
        q.registerServer(sid,server)

    for e in c:
        e.start()
    for e in s:
        e.start()

if __name__ == '__main__':
    main()
