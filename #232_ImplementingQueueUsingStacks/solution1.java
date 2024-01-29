// Method: Use 2 stacks
// TC: O(n)
// SC: O(n)

class MyQueue {

    private Deque<Integer> s1;
    private Deque<Integer> s2;
    private int front;

    public MyQueue() {
        front = 0;
        s1 = new ArrayDeque<>();
        s2 = new ArrayDeque<>();
    }
    
    // TC: O(1), SC: O(n)
    public void push(int x) {
        if (s1.isEmpty()) {
            front = x;
        }
        s1.push(x);
    }
    
    // TC: O(1) amortized and O(n) worst-case, SC: O(1)
    public int pop() {
        if (s2.isEmpty()) {
            while (!s1.isEmpty()) {
                s2.push(s1.pop());
            }
        }
        return s2.pop();
    }
    
    // TC: O(1), SC: O(1)
    public int peek() {
        if(!s2.isEmpty()) {
            return s2.peek();
        }
        return front;
    }
    
    // TC: O(1), SC: O(1)
    public boolean empty() {
        return s1.isEmpty() && s2.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */