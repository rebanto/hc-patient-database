import libsql_client

def stringEscape(variable):
    return "\"" + variable + "\""
        

def deletePerson(name):
    with libsql_client.create_client_sync(
        "libsql://patientdata-heyingz.turso.io",
        auth_token="eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MzEyNTY3NzEsImlkIjoiMzg0YTcxYzQtODA3OS00NDYyLWI3MzktZDNmZWUxOGU4MzAzIn0.Dy6ULddDvLPfHKi77E9L85IfAZ-svnGynCXLQRlDuH4hSABwT7ixlNYfxE02jn35yHp3L1FZC9D4L64KpxpiCg"
    ) as client:
        command = "DELETE FROM Patient WHERE first_name = \"" + name +"\""
        result = client.execute(command)

def addPerson(id, fname, lname, dob):
    with libsql_client.create_client_sync(
        "libsql://patientdata-heyingz.turso.io",
        auth_token="eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MzEyNTY3NzEsImlkIjoiMzg0YTcxYzQtODA3OS00NDYyLWI3MzktZDNmZWUxOGU4MzAzIn0.Dy6ULddDvLPfHKi77E9L85IfAZ-svnGynCXLQRlDuH4hSABwT7ixlNYfxE02jn35yHp3L1FZC9D4L64KpxpiCg"
    ) as client:
        command = "INSERT INTO patient_data (ID, first_name, last_name, DOB) VALUES (\"" + str(id) + "\", \"" + fname + "\", \"" + lname + "\", \"" + dob + "\");"
        result = client.execute(command)


        
def addVitals(id, temperature, pain_level, blood_pressure, pulse, resp_rate, oxygen, time):
    with libsql_client.create_client_sync(
    "libsql://patientdata-heyingz.turso.io",
    auth_token="eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MzEyNTY3NzEsImlkIjoiMzg0YTcxYzQtODA3OS00NDYyLWI3MzktZDNmZWUxOGU4MzAzIn0.Dy6ULddDvLPfHKi77E9L85IfAZ-svnGynCXLQRlDuH4hSABwT7ixlNYfxE02jn35yHp3L1FZC9D4L64KpxpiCg"
    ) as client:
        command = "INSERT INTO vitals(ID, temperature, pain_level, blood_pressure, pulse, resp_rate, oxygen, time) VALUES ("+ str(id) +","+ str(temperature) +"," +str(pain_level) +","+ stringEscape(blood_pressure) +","+ str(pulse) +"," + str(resp_rate) +","+ str(oxygen) +"," + stringEscape(time)+");"
        print(command)
        result = client.execute(command)       
def readTable(table):
    with libsql_client.create_client_sync(
    "libsql://patientdata-heyingz.turso.io",
    auth_token="eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MzEyNTY3NzEsImlkIjoiMzg0YTcxYzQtODA3OS00NDYyLWI3MzktZDNmZWUxOGU4MzAzIn0.Dy6ULddDvLPfHKi77E9L85IfAZ-svnGynCXLQRlDuH4hSABwT7ixlNYfxE02jn35yHp3L1FZC9D4L64KpxpiCg"
    ) as client:
        result_set = client.execute("SELECT * from " + table)
        print(len(result_set.rows), "rows")
        for row in result_set.rows:
            print(row)

def addBed(id, bedNum, start):
    with libsql_client.create_client_sync(
    "libsql://patientdata-heyingz.turso.io",
    auth_token="eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MzEyNTY3NzEsImlkIjoiMzg0YTcxYzQtODA3OS00NDYyLWI3MzktZDNmZWUxOGU4MzAzIn0.Dy6ULddDvLPfHKi77E9L85IfAZ-svnGynCXLQRlDuH4hSABwT7ixlNYfxE02jn35yHp3L1FZC9D4L64KpxpiCg"
    ) as client:
        command = "INSERT INTO room(ID, bed_number, start_time, end_time) VALUES ("+ str(id) +","+ str(bedNum) +" , " + stringEscape(start) +", " + stringEscape("x")+");"
        result = client.execute(command)




addPerson(1234, "Pranav", "Sreepada", "December 4, 2009")
