import React from 'react';
import './Header.css';
import { IoLibraryOutline } from 'react-icons/io5';

var title = "{ FiloStack }"


class Header extends React.Component {
    render() {
        return (
            <div className="container" >
                <div className="left-container">
                    <IoLibraryOutline className="logo" alt="Logo" />
                </div>
                <div className="center-container">
                    <h1 className="title"> {title} </h1>
                </div>
                <div className="right-container">
                    <input type="text" className="search" placeholder="Pesquisar" />
                </div>
            </div>
        );
    }
};
export default Header;