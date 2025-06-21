import React, { useEffect, useState } from 'react';
import axios from 'axios';

const BookListPage = ({ token }) => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/books', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }).then((res) => setBooks(res.data));
  }, [token]);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Liste des Livres</h1>
      <ul className="space-y-2">
        {books.map((book) => (
          <li key={book.id} className="bg-white shadow p-2 rounded">
            <strong>{book.title}</strong> — {book.author}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BookListPage;
