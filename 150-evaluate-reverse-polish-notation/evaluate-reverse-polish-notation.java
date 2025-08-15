class Solution {
    public int evalRPN(String[] tokens) {

        //stack, 2 numbers then operator : calculate result and put in stack, search for next operator keeo stacking
        Stack<Integer> myStack = new Stack<>();
        int val1 = 0;
        int val2 = 0;
        int result = 0;
        for (String token : tokens) {
            if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
                val2 = myStack.pop();
                val1 = myStack.pop();
                if (token.equals("+")) {
                    result = val1 + val2;
                } else if (token.equals("-")) {
                    result = val1 - val2;
                } else if (token.equals("*")) {
                    result = val1 * val2;
                } else if (token.equals("/")) {
                    result = val1 / val2; // integer division
                }
            myStack.push(result);
            }

            else {
                myStack.push(Integer.parseInt(token));
            }
        }
        return myStack.pop();

    }
}