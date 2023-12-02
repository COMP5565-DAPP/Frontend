import React, { createContext, useState, useContext } from 'react';

// 创建用户上下文
const UserContext = createContext(null);

// 用户提供者组件，用于提供用户信息和角色
export const UserProvider = ({ children }) => {
  // 从 localStorage 中获取用户信息

  const [user, setUser] = useState(JSON.parse(localStorage.getItem('currentUser')));
  const [role, setRole] = useState("");
  const [address, setAddress] = useState("");

  // login function for setting user info
  const login = (userData) => {
    setUser(userData); // 设置用户信息
    setRole(userData.role); // 设置用户角色
    setAddress(userData.address); // 设置用户地址
  };

  // provide the user object and login function through the context
  return (
    <UserContext.Provider value={{ setUser, login, user, role,address }}>
      {children}
    </UserContext.Provider>
  );
};

// 自定义 hook 用于访问用户上下文
export const useUser = () => {
  return useContext(UserContext);
};

export default UserContext;
