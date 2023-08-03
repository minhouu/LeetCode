class Solution {
    public int calculate(String s) {
        // use stack
        // first num -> always add to result
        // since second num -> check what operator precedes
        // if multiplication or division precedes -> calcurate the number with lastNum and push again
        // if addition or substraction precedes -> just push +(num) or -(num)


        int curNum = 0;
        int result = 0;
        int lastNum = 0;
        char oper = '+'; // set init oper '+' (first number always eqauls to +num)

        for (int i = 0; i < s.length(); i++) {
            char curChar = s.charAt(i);
            // when curChar is digit
            if(Character.isDigit(curChar)) {
                curNum = (curNum * 10) + (curChar - '0');
            }
            // when curChar is not /s or i reached end of string
            if (!Character.isDigit(curChar) && !Character.isWhitespace(curChar) || i == s.length()-1){               
                if (oper == '+' || oper == '-') {
                    result += lastNum;
                    lastNum = (oper == '+')? curNum : - curNum; 
                }
                else if (oper == '*') {
                    lastNum = lastNum * curNum;
                }
                else if (oper == '/') {
                    lastNum = lastNum / curNum;
                }
                oper = curChar; // set operator to calculate next integer
                curNum = 0;
            }
        }
        result += lastNum;
        return result;
    }
    
}
