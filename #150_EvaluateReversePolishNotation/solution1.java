// Method: Use stack (ArrayDeque)
// TC: O(n)
// SC: O(n)
class Solution {
    public int evalRPN(String[] tokens) {
        Deque<String> stack = new ArrayDeque<>();

        for (int i = 0; i < tokens.length; i++) {
            if (tokens[i].matches("-?\\d+(\\.\\d+)?")) {
                stack.push(tokens[i]);
            } else {
                int num2 = Integer.parseInt(stack.pop());
                int num1 = Integer.parseInt(stack.pop());
                
                int result = 0;
                if (tokens[i].equals("+")) {
                    result = num1 + num2;
                } else if (tokens[i].equals("-")) {
                    result = num1 - num2;
                } else if (tokens[i].equals("*")) {
                    result = num1 * num2;
                } else {
                    result = num1 / num2;
                }
                stack.push(Integer.toString(result));
            }
        }
        return Integer.parseInt(stack.pop());
    }
}