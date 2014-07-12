//~~more than 5kb to be modified
//it seems that I misunderstood the question
//
#include <stdio.h>
#include <string.h>
#define ll long long int

int N, i, j, keyLen, textLen, tmp, tag, nr1, nr2, nr3, ntag; //(N<1000)

char keyArr[9], first;
int keyIndexArr[9];
int numOfEveryColumn[9];
char plaintext[250];
char output[250];


inline void fast_scanstr(char *str)
{
    register char c=0;
    register int i = 0;
    while (c < 33)
        c = getchar_unlocked();
    while (c >= 48)
    {
        str[i] = c;
        c = getchar_unlocked();
        i = i + 1;
    }
    str[i] = '\0';
}
void getIndexOfKey(char *key, int *keyIndex)
{  
    int i, j, len=strlen(key);
    for (i = 0; i < len; ++i)
    {
        for (j = 0; j < len; ++j)
        {
            if(key[j] == i+49){
				keyIndex[i] = j; 
				break;
			}
        }
        // printf("%d", keyIndex[i]);
    }
    // printf("\n");
}
void getNumOfRowAndColumn(int keyLen, int textLen, int *numOfEveryColumn)
{
    int mod, factor;
    if(keyLen&1)
    {
        mod = textLen%(3*keyLen);
        factor = textLen/(3*keyLen)*2;
        // printf("%d %d\n", mod, factor);
        if(mod == 0){
            for (i = 0; i < keyLen; ++i) numOfEveryColumn[i] = factor;
        }else if(mod < ((3*keyLen+1)/2)){
            for (i = 0; i < keyLen; ++i)
            {
                numOfEveryColumn[i] = factor;
                if(((i&1) && (3*(i+1)/2<=mod) || (!(i&1) && (3*i/2+2)<=mod)))
                    numOfEveryColumn[i]++;
            }
        }else if(mod == ((3*keyLen+1)/2)){
            for (i = 0; i < keyLen; ++i)
            {
                numOfEveryColumn[i] = factor+1;
            }           
        }else{
            mod = mod-(3*keyLen+1)/2;
            // printf("%d\n", mod);
            for (i = 0; i < keyLen; ++i)
            {
                numOfEveryColumn[i] = factor+1;
                if(((i&1) && (3*i+1)/2<=mod) || (!(i&1) && (3*i/2+1)<=mod))
                    numOfEveryColumn[i]++;
            }            
        }
    }else{
        mod = textLen%(3*keyLen/2);
        factor = textLen/(3*keyLen/2);
        if (mod == 0){
            for (i = 0; i < keyLen; ++i) numOfEveryColumn[i] = factor;
        }else{
            for (i = 0; i < keyLen; ++i)
            {
                numOfEveryColumn[i] = factor;
                if(factor&1){
                    if(((i&1) && (3*i+1)/2<=mod) || (!(i&1) && (3*i/2+1)<=mod))
                        numOfEveryColumn[i]++;
                }else{
                    if(((i&1) && (3*(i+1)/2<=mod) || (!(i&1) && (3*i/2+2)<=mod)))
                        numOfEveryColumn[i]++;
                }
            }            
        }
    }
    // for (i = 0; i < keyLen; ++i) printf("%d", numOfEveryColumn[i]);
    // printf("\n");
}
int main()
{
    freopen("AMSCO1.txt", "r", stdin);

    while(1)
    {
        if((first=getchar()) == EOF) break;
        else{
            keyArr[0] = first;
            fast_scanstr(keyArr+1);
            fast_scanstr(plaintext);
            // printf("%s\n", keyArr);
            // printf("%s\n", plaintext);
            getIndexOfKey(keyArr, keyIndexArr);
            keyLen = strlen(keyArr);
            textLen = strlen(plaintext);
            getNumOfRowAndColumn(keyLen, textLen, numOfEveryColumn);
            // printf("%d %d\n", nr1, nr2);
            if(keyLen&1){
                nr1 = (3*keyLen+1)/2;
                nr2 = nr1 - 1;
                for (i = 0; i < keyLen; ++i)
                {
                    if(keyIndexArr[i]&1){
                        tmp = (3*keyIndexArr[i]+1)/2;
                        tag = 1;
                        for (j = 0; j < numOfEveryColumn[keyIndexArr[i]]; ++j)
                        {
                            if (tag) {
                                printf("%c",  plaintext[tmp]);
                                tmp += nr2; tag = 0;
                            }else {
                                printf("%c%c",plaintext[tmp],plaintext[tmp+1]);
                                tmp += nr1; tag = 1;
                            }
                        }
                    }else{
                        tmp = (3*keyIndexArr[i])/2;
                        tag = 1;
                        for (j = 0; j < numOfEveryColumn[keyIndexArr[i]]; ++j)
                        {
                            if (tag) {
                                printf("%c%c", plaintext[tmp],plaintext[tmp+1]);
                                tmp += nr1; tag = 0;
                            }else {
                                printf("%c", plaintext[tmp]);
                                tmp += nr2; tag = 1;
                            }
                        }                    
                    }
                    // printf("\n");
                }
            }else{
                nr2 = 3*keyLen/2;
                nr1 = nr2 - 1;
                nr3 = nr2 + 1;
                for (i = 0; i < keyLen; ++i)
                {
                    if(keyIndexArr[i]&1){
                        tmp = (3*keyIndexArr[i]+1)/2;
                        tag = 1; ntag = 1;
                        for (j = 0; j < numOfEveryColumn[keyIndexArr[i]]; ++j)
                        {
                            if (tag) {
                                printf("%c",  plaintext[tmp]);
                                tag = 0;
                                if(ntag%3 == 1) tmp += nr1;
                                if(ntag%3 == 2) tmp += nr3;
                                if(ntag%3 == 0) tmp += nr2;
                                ntag++;
                            }else {
                                printf("%c%c",  plaintext[tmp],plaintext[tmp+1]);
                                tag = 1;
                                if(ntag%3 == 1) tmp += nr1;
                                if(ntag%3 == 2) tmp += nr3;
                                if(ntag%3 == 0) tmp += nr2;
                                ntag++;
                            }
                        }
                    }else{
                        tmp = (3*keyIndexArr[i])/2;
                        tag = 1;
                        for (j = 0; j < numOfEveryColumn[keyIndexArr[i]]; ++j)
                        {
                            if (tag) {
                                printf("%c%c", plaintext[tmp],plaintext[tmp+1]);
                                tmp += nr2; tag = 0;
                            }else {
                                printf("%c", plaintext[tmp]);
                                tmp += nr2; tag = 1;
                            }
                        }                    
                    }
                    // printf("\n");
                }               
            }
            printf("\n");
        }
    }
    fclose(stdin);
    return 0;
}
