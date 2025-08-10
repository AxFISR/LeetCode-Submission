class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //key will be array the size of 26
        //value will be the list of words
        HashMap<String, List<String>> myMap = new HashMap<String, List<String>>();

        
        int len = strs.length;
        for(int i = 0 ; i < len ; i++){
            int[] key = new int[26];
            for(int j = 0 ; j < strs[i].length() ; j++){
                key[strs[i].charAt(j) - 'a']++;
            }
            String myKey = Arrays.toString(key);
            if(myMap.containsKey(myKey)){
                myMap.get(myKey).add(strs[i]);
            }
            else{
                List<String> val = new ArrayList<>();
                myMap.put(myKey, val);
                myMap.get(myKey).add(strs[i]);
            }
        }
        List<List<String>> returnVal = new ArrayList<List<String>>();

        for (List<String> value : myMap.values()) {
            returnVal.add(value);
        }
        return returnVal;

    }
}