"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
"""



class MyQueue {

    /** Initialize your data structure here. */
    var stack:[Int] = []
    init() {
        
        
    }
    
    /** Push element x to the back of queue. */
    func push(_ x: Int) {
        
        self.stack.append(x)
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    func pop() -> Int {
        
        let ele = self.stack[0]
        
        self.stack.remove(at:0)
        return ele
        
    }
    
    /** Get the front element. */
    func peek() -> Int {
        
        return self.stack[0]
        
    }
    
    /** Returns whether the queue is empty. */
    func empty() -> Bool {
        
        if self.stack.count == 0{
            return true
        }
        else{
            return false
        }
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue()
 * obj.push(x)
 * let ret_2: Int = obj.pop()
 * let ret_3: Int = obj.peek()
 * let ret_4: Bool = obj.empty()
 */
