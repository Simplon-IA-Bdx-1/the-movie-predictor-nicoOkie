import argparse
import sys
import csv

class Parser(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description="The Moviepredictor CLI",
            usage='''app.py <context> <command> [<args>]

The context can be: people | movie
The commands are:
    list        List the entities
    find        Find one entity by Id
    import      Create DB entries from external sources
    insert      Insert one enity by hand
    scrap       Scrap the web with a URL
''')
        parser.add_argument("context", help="The context in wich the command will be execute")
        parser.add_argument("command", help="The command to run")
        args = parser.parse_args(sys.argv[1:3])
        self.context = args.context
        self.command = args.command
        
        getattr(self, args.command)()

    def list(self):
        parser = argparse.ArgumentParser(
            description="List the entities in database"
        )
        parser.add_argument("--export", help="Chemin vers le fichier a exporter, format csv")
        args = parser.parse_args(sys.argv[3:4])
        if self.context == "people":
            people = db.find_all("people")
            if args.export:
                with open(args.export, 'w', encoding='utf-8', newline='\n') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(people[0].keys())
                    for person in people:
                        writer.writerow(person.values())
            else:
                for person in people:
                    db.print_person(person)
