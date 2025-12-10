bool isAnagram(char* s, char* t) {
    //counting array solution, one increment and other decrement , when all values are 0 its anagram
    int myArr[26] = {0};
    if (strlen(t) != strlen(s)){
        return false;
    }
    for (int i = 0 ; i < strlen(s) ; i++){
        myArr[s[i] - 'a']++;
        myArr[t[i] - 'a']--;
    }
    for(int j = 0 ; j <26 ; j++){
        if( myArr[j] != 0 ){
            return false;
        }

    }
    return true;
}