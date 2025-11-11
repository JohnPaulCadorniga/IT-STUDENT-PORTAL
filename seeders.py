from app import app
from models.db import db
from models.user_model import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def seed_data():
    with app.app_context():
        try:
            print("Starting database seeding")
            
            seed_users = [
                User (
                    fname="Admin",
                    lname="User",
                    uname="admin",
                    email="admin@example.com",
                    pass_word=generate_password_hash("admin123"),
                    birthday="2002-11-11",
                    gender="male",
                    phone_number="09191234567",
                    address="lot 4 papaya st., greenland, cainta, rizal",
                    student_id="2021-12322-mn-0",
                ),
                User (
                    fname="Chelsy",
                    lname="Paralejas",
                    uname="chelsykai",
                    email="chelsykai@test.com",
                    pass_word=generate_password_hash("pass123"),
                    birthday="2003-10-23",
                    gender="female",
                    phone_number="09193219283",
                    address="63 anonas st., maui oasis, sta. mesa, manila",
                    student_id="2022-22398-mn-0",
                )
            ]
        
            for user in seed_users:
                existing_user = User.query.filter_by(email=user.email).first()
                if existing_user:
                    print(f"Skipping existing user: {user.email}")
                    continue
                db.session.add(user)
                    
            db.session.commit()
            print("Database seeded successfully")
                
        except IntegrityError as e:
            db.session.rollback()
            print(f"Integrity error: {e}")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"SQLAchemy error: {e}")

        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error during seeding: {e}")

        finally:    
            db.session.close()

if __name__ == "__main__":
    seed_data()