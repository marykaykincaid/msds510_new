# Mary Kay Kincaid
# 4/7/18
# Assignment 9.1 - Week 9 - OOP
# Object Oriented Programming Assignment

from datetime import datetime


class Avenger:
    def __init__(self, record):
        """
        Initializes the object with a dictionary-based record.
        Args:
            record (dict): Dictionary-based record of Avenger data
        """
        self.record = record

    def url(self):
        """
        Returns:
            str: The URL of the comic character on the Marvel Wikia
        """
        return self.record.get('url')

    def name_alias(self):
        """
        Returns:
            str: The full name or alias of the character
        """
        return self.record.get('name_alias')

    def appearances(self):
        """
        Returns:
            int: The number of comic books that character appeared in as of April 30
        """
        return int(self.record.get('appearances'))

    def is_current(self):
        """
        Returns:
            bool: Is the member currently active on an avengers affiliated team? (True/False)
        """
        return bool(self.record.get('current'))

    def gender(self):
        """
        Returns:
            str: The recorded gender of the character
        """
        return self.record.get('gender')

    def year(self):
        """
        Returns:
            int: The year the character was introduced as a full or reserve member of the Avengers
        """
        return self.record.get('year')

    def full_reserve_avengers_intro(self):
        """
        Returns:
            int: The year the character was introduced as a full or reserve member of the Avengers
        """
        return self.record.get('full_reserve_avengers_intro')

    def date_joined(self):
        """
        Returns:
            datetime.date: The date the character joined
        """
        d = self.full_reserve_avengers_intro()
        new_d = datetime.strptime(d, '%b-%y')
        day = str(new_d.day)
        month = str(new_d.month)
        year = str(self.year())
        new_date_string = month + '-' + day + '-' + year
        date_joined = datetime.strptime(new_date_string, '%m-%d-%Y')
        # new_date = datetime.strftime(new_date, '%m-%d-%Y')
        date_joined = datetime.date(date_joined)
        new_year = date_joined.year
        new_month = date_joined.month
        new_day = date_joined.day
        return date_joined

    def days_since_joining(self):
        """
        Returns:
            int: The number of integer days since the character joined
        """
        d = self.full_reserve_avengers_intro()
        new_d = datetime.strptime(d, '%b-%y')
        day = str(new_d.day)
        month = str(new_d.month)
        year = str(self.year())
        new_date_string = month + '-' + day + '-' + year

        join_date = datetime.strptime(new_date_string, '%m-%d-%Y')

        join_date = datetime.date(join_date)
        current_date = datetime.today()
        current_date = datetime.date(current_date)

        days_since_joining = (current_date - join_date).days
        return days_since_joining

    def years_since_joining(self):
        """
        Returns:
            int: The number of integer years since the character joined
        """
        current_year = datetime.today()
        current_year = current_year.year
        return current_year - int(self.record.get('year'))

    def notes(self):
        """STRIP OFF TRAILING NEWLINES AND SPACES
        Returns:
            str: Descriptions of deaths and resurrections.
        """
        return self.record.get('notes').rstrip().strip('\n')

    def __str__(self):
        """
        Returns:
            str: A human-readable value for this character
        """
        return '%s' % self.record

    def __repr__(self):
        """
        Returns:
            str: String representation of object.  Useful for debugging.
        """
        return 'Avenger(name_alias = %s, url = %s)'% (self.name_alias(), self.url())
        # return 'Avenger: %s' % (self.record)
        # return "%s(%r)" % (self.__class__, self.__dict__)


if __name__ == '__main__':
    pym_record = {
        'name_alias': 'Henry Jonathan "Hank" Pym',
        'url': 'http://marvel.wikia.com/Henry_Pym_(Earth-616)',
        'appearances': '1269',
        'current': 'YES',
        'death1': 'YES',
        'death2': '',
        'death3': '',
        'death4': '',
        'death5': '',
        'full_reserve_avengers_intro': 'Sep-63',
        'gender': 'MALE',
        'honorary': 'Full',
        'notes': 'Merged with Ultron in Rage of Ultron Vol. 1. A funeral was held. \n',
        'probationary_introl': '',
        'return1': 'NO',
        'return2': '',
        'return3': '',
        'return4': '',
        'return5': '',
        'year': '1963',
        'years_since_joining': '52'
    }

    hank_pym = Avenger(pym_record)
    print('Name/Alias: {}'.format(hank_pym.name_alias()))
    print('URL: {}'.format(hank_pym.url()))
    print('Number of Appearances: {}'.format(hank_pym.appearances()))
    print('Is Current?: {}'.format(hank_pym.is_current()))
    print('Gender: {}'.format(hank_pym.gender()))
    print('Year Joined: {}'.format(hank_pym.year()))
    print('Date Joined: {}'.format(hank_pym.date_joined()))
    print('Days Since Joined: {}'.format(hank_pym.days_since_joining()))
    print('Years Since Joined: {}'.format(hank_pym.years_since_joining()))
    print('Notes: {}'.format(hank_pym.notes()))
    print('__str__: {}'.format(hank_pym))
    print('__repr__: {}'.format(hank_pym.__repr__()))
