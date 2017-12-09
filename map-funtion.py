people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    #print(title)
    lastname = person.split()[-1]
    print(lastname)
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))