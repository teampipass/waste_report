import React, { useState } from 'react';
import LoginPage from './pages/LoginPage';
import BookListPage from './pages/BookListPage';

const App = () => {
  const [user, setUser] = useState(null);

  return user ? (
    <BookListPage token={user.access_token} />
  ) : (
    <LoginPage onLogin={setUser} />
  );
};

export default App;
