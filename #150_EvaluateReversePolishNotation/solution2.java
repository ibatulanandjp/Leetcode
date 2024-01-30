// Method: Use stack (array)
// TC: O(n)
// SC: O(n)
class Solution {
    public int evalRPN(String[] tokens) {
        int[] stack = new int[tokens.length];
        int top = 0;

        for (String token : tokens) {
            if (token.equals("+")) {
                int n2 = stack[--top];
                int n1 = stack[--top];
                stack[top++] = n1 + n2;
            } else if (token.equals("-")) {
                int n2 = stack[--top];
                int n1 = stack[--top];
                stack[top++] = n1 - n2;
            } else if (token.equals("*")) {
                int n2 = stack[--top];
                int n1 = stack[--top];
                stack[top++] = n1 * n2;
            } else if (token.equals("/")) {
                int n2 = stack[--top];
                int n1 = stack[--top];
                stack[top++] = n1 / n2;
            } else {
                stack[top++] = Integer.parseInt(token);
            }
        }
        return stack[0];
    }
}