stronomical_hour = 60  
academical_hour = 40  
academical_hour_total = 64  
session_academical_hours = 4  
session_break = 20  

sessions = academical_hour_total / session_academical_hours

total_academical_minutes = academical_hour_total * academical_hour

total_break_minutes = sessions * session_break

total_time_minutes = total_academical_minutes + total_break_minutes

total_time_astronomical_hours = total_time_minutes / stronomical_hour

print(f"Обща продължителност в астрономически часове: {total_time_astronomical_hours:.2f}")









