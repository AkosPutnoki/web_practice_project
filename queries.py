import common


def mentor_names():
    names = common.query_handler("""SELECT id, CONCAT(first_name, ' ', last_name) AS full_name
                                    FROM mentors
                                    ORDER BY first_name""")
    return names


def mentor_info(mentor_id):
    info = common.query_handler("""SELECT CONCAT(first_name, ' ', last_name) AS full_name, nick_name, phone_number,
                                    email, city, favourite_number
                                    FROM mentors
                                    WHERE id = %s""", (mentor_id,))
    return info

def applicant_info():
    info = common.query_handler("""SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number, email, application_code
                                    FROM applicants
                                    ORDER BY first_name""")
    return info


def save_applicant(formdata):
    common.query_handler("""INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                            VALUES (%s, %s, %s, %s, %s)""", (formdata['first_name'], formdata['last_name'], 
                            formdata['phone_number'], formdata['email'], formdata['application_code']), result=False)


def school_info():
    info = common.query_handler("""SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) AS mentor_name,
                                    name, schools.city, schools.country, image, description FROM schools
                                    INNER JOIN mentors ON mentors.id = schools.contact_person
                                    ORDER BY country, city""")
    return info