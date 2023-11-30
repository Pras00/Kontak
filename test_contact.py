import unittest
from unittest.mock import patch
from io import StringIO
from contact import ContactManager

class TestContactManager(unittest.TestCase):
 
    def setUp(self):
        self.contact_manager = ContactManager()

    # Create Contact

    def test_create_contact(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.create_contact("Prass", "082135776489")
        expected_output = "Kontak 'Prass' dengan nomor '082135776489' berhasil ditambahkan."
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    # Show Contact

    def test_show_contact(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.create_contact("Prass", "1234567890")
        expected_output = "Kontak 'Prass' dengan nomor '1234567890' berhasil ditambahkan."
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.show_contact()
        expected_output = "Daftar Kontak:\n1. Nama: Prass, Nomor Telepon: 1234567890"
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    def test_show_contact_empty(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.show_contact()
        expected_output = "Daftar kontak kosong."
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    # Search Contact

    def test_search_contact_found(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.create_contact("Prass", "1234567890")
        expected_output = "Kontak 'Prass' dengan nomor '1234567890' berhasil ditambahkan."
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.search_contact("Prass")
        expected_output = "Kontak ditemukan:\nNama: Prass, Nomor Telepon: 1234567890"
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    def test_search_contact_not_found(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.search_contact("Adin")
        expected_output = "Kontak dengan nama Adin tidak ditemukan."
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    # Edit Contact

    def test_edit_contact(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.create_contact("Prass", "1234567890")
        expected_output = "Kontak 'Prass' dengan nomor '1234567890' berhasil ditambahkan."
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

        with patch('builtins.input', side_effect=['9999999999']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.contact_manager.edit_contact("Prass")
        expected_output = "Nomor telepon kontak Prass berhasil diperbarui."
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    def test_edit_contact_not_found(self):
        with patch('builtins.input', side_effect=['9999999999']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.contact_manager.edit_contact("Adin")
        expected_output = "Kontak dengan nama Adin tidak ditemukan."
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    # Delete Contact

    def test_delete_contact_found(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.create_contact("Prass", "1234567890")
        expected_output = "Kontak 'Prass' dengan nomor '1234567890' berhasil ditambahkan."
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.delete_contact("Prass")
        expected_output = f"Kontak dengan nama Prass berhasil dihapus."
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    def test_delete_contact_not_found(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.delete_contact("Adin")
        expected_output = "Kontak dengan nama Adin tidak ditemukan."
        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    # Full Function

    def test_create_edit_search_show_delete(self):

        # Create Contact
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.create_contact("Prass", "123456789")
        create_output = mock_stdout.getvalue().strip()
        self.assertEqual(create_output, "Kontak 'Prass' dengan nomor '123456789' berhasil ditambahkan.")

        # Edit Contact
        with patch('builtins.input', side_effect=["987654321"]), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.edit_contact("Prass")
        edit_output = mock_stdout.getvalue().strip()
        self.assertEqual(edit_output, "Nomor telepon kontak Prass berhasil diperbarui.")

        # Search Contact
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.search_contact("Prass")
        search_output = mock_stdout.getvalue().strip()
        expected_search_result = "Kontak ditemukan:\nNama: Prass, Nomor Telepon: 987654321"
        self.assertEqual(search_output, expected_search_result)

        # Show Contact
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.show_contact()
        show_output = mock_stdout.getvalue().strip()
        expected_show_result = "Daftar Kontak:\n1. Nama: Prass, Nomor Telepon: 987654321"
        self.assertEqual(show_output, expected_show_result)

        # Delete Contact
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.delete_contact("Prass")
        delete_output = mock_stdout.getvalue().strip()
        self.assertEqual(delete_output, "Kontak dengan nama Prass berhasil dihapus.")

        # Show Contact
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contact_manager.show_contact()
        show_after_delete_output = mock_stdout.getvalue().strip()
        self.assertEqual(show_after_delete_output, "Daftar kontak kosong.")


if __name__ == '__main__':
    unittest.main()
