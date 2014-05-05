#include <string.h>

#ifndef STRING_H_ 
#define STRING_H_
char * strcat(char* s, char*t){
    char *cptr = s;
    while(*cptr)
        cptr++;
    while( cptr < s + strlen(s) &&  *cptr++=*t++)
        ;
    return s;
}

/* if the string s ends with string t, the function return 1, otherwise 0;
 */
int strend(const char*s, const char* t){
    char *sptr = s;
    char *tptr = t;

    while(*sptr)
        sptr++;
    while(*tptr)
        tptr++;
    while( tptr <= t && sptr <= s && *--sptr == *--tptr);

    if( tptr== t && *tptr = *sptr)
        return 1;
    else
        return 0;
}

int strend2(const char*s, const char*t){
    char *i;
    i = s + strlen(s) - strlen(t);
    while(*i && *i == *t++)
        i++;
    if(*i == '\0')
        return 1;
    else 
        return 0;
}
#endif
