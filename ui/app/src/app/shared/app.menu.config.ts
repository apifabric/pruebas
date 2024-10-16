import { MenuRootItem } from 'ontimize-web-ngx';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { ExpiryCardComponent } from './Expiry-card/Expiry-card.component';

import { FruitCardComponent } from './Fruit-card/Fruit-card.component';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderDetailCardComponent } from './OrderDetail-card/OrderDetail-card.component';

import { PromotionCardComponent } from './Promotion-card/Promotion-card.component';

import { SaleCardComponent } from './Sale-card/Sale-card.component';

import { SaleDetailCardComponent } from './SaleDetail-card/SaleDetail-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';

import { SupplierFruitCardComponent } from './SupplierFruit-card/SupplierFruit-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'Expiry', name: 'EXPIRY', icon: 'view_list', route: '/main/Expiry' }
    
        ,{ id: 'Fruit', name: 'FRUIT', icon: 'view_list', route: '/main/Fruit' }
    
        ,{ id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderDetail', name: 'ORDERDETAIL', icon: 'view_list', route: '/main/OrderDetail' }
    
        ,{ id: 'Promotion', name: 'PROMOTION', icon: 'view_list', route: '/main/Promotion' }
    
        ,{ id: 'Sale', name: 'SALE', icon: 'view_list', route: '/main/Sale' }
    
        ,{ id: 'SaleDetail', name: 'SALEDETAIL', icon: 'view_list', route: '/main/SaleDetail' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
        ,{ id: 'SupplierFruit', name: 'SUPPLIERFRUIT', icon: 'view_list', route: '/main/SupplierFruit' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    CustomerCardComponent

    ,EmployeeCardComponent

    ,ExpiryCardComponent

    ,FruitCardComponent

    ,InventoryCardComponent

    ,OrderCardComponent

    ,OrderDetailCardComponent

    ,PromotionCardComponent

    ,SaleCardComponent

    ,SaleDetailCardComponent

    ,SupplierCardComponent

    ,SupplierFruitCardComponent

];