/* given a day and a year, convert them to a date.
 * e.g: month_day(2000,60, &m, &d) m=2, d=29
 */

#include <stdio.h>

static char daytab[2][13] ={
    {0,31,28,31,30,31,30,31,31,30,31,30,31},
    {0,31,29,31,30,31,30,31,31,30,31,30,31}
};

void month_day(int year, int days, int* month, int* d){
    int leap, i;
    leap = (year%400==0 || year%100!=0 && year%4==0);

    for(i=1; days>daytab[leap][i];++i)
        days -= daytab[leap][i];

    *month = i;
    *d = days;
}

int day_of_year(int years, int month, int days){
    int leap, i;

    leap = years % 400 || years % 4 == 0 && years % 100 != 0;

    for(i=1;i<month;++i)
        days += daytab[leap][i];

    return days;
}

int main(int argc, char* argv[]){
    int year, days, month, day;
    int cmonth, cday;
    year = 1988;
    days = 60;
    month = 2;
    day = 29;

    month_day(year, days, &cmonth, &cday);
    printf("%d %dth day is %dnd month, %dth day\n", year, days, cmonth, cday);
    printf("%dnd month, %dth day in %d year is %d days\n", month, day, year, day_of_year(year, month, day));

    return 0;
}
