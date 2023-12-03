import React, { createContext, useState, useContext } from 'react';

const UserContext = createContext(null);
export const UserProvider = ({ children }) => {

  // get info of user from localStorage if it exists
  const [user, setUser] = useState(JSON.parse(localStorage.getItem('currentUser')));
  const [role, setRole] = useState("");
  const [address, setAddress] = useState("");
  // login function for setting user info
  const login = (userData) => {
    setUser(userData); 
    setRole(userData.role); 
    setAddress(userData.address); 
  };
  // provide the user object and login function through the context
  return (
    <UserContext.Provider value={{ setUser, login, user, role,address }}>
      {children}
    </UserContext.Provider>
  );
  
};

// hook for using the context
export const useUser = () => {
  return useContext(UserContext);
};

export default UserContext;
