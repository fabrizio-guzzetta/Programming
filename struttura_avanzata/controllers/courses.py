from models.course import create


def handle_creation(data):
    if data['name'] != 'gigi':
        create(
            name=data['name'],
            cls=data['class'],
        )

        return True
    
    return False
