class Solution {
    public boolean isPalindrome(String s) {
        if(s.length() <= 1){
            return true;
        }
        String noSpace = new String();
        String lowerCase = new String();
        noSpace = s.replaceAll("[^a-zA-Z0-9]", ""); // remove spaces
        lowerCase = noSpace.toLowerCase(); //lower casing everything

        int left = 0;                   //left pointer
        int right = lowerCase.length() - 1; //right pointer

        while(left < right){
            if(lowerCase.charAt(left) != lowerCase.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}