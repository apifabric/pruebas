import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FruitHomeComponent } from './home/Fruit-home.component';
import { FruitNewComponent } from './new/Fruit-new.component';
import { FruitDetailComponent } from './detail/Fruit-detail.component';

const routes: Routes = [
  {path: '', component: FruitHomeComponent},
  { path: 'new', component: FruitNewComponent },
  { path: ':id', component: FruitDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Fruit-detail-permissions'
      }
    }
  },{
    path: ':fruit_id/Expiry', loadChildren: () => import('../Expiry/Expiry.module').then(m => m.ExpiryModule),
    data: {
        oPermission: {
            permissionId: 'Expiry-detail-permissions'
        }
    }
},{
    path: ':fruit_id/Inventory', loadChildren: () => import('../Inventory/Inventory.module').then(m => m.InventoryModule),
    data: {
        oPermission: {
            permissionId: 'Inventory-detail-permissions'
        }
    }
},{
    path: ':fruit_id/OrderDetail', loadChildren: () => import('../OrderDetail/OrderDetail.module').then(m => m.OrderDetailModule),
    data: {
        oPermission: {
            permissionId: 'OrderDetail-detail-permissions'
        }
    }
},{
    path: ':fruit_id/Promotion', loadChildren: () => import('../Promotion/Promotion.module').then(m => m.PromotionModule),
    data: {
        oPermission: {
            permissionId: 'Promotion-detail-permissions'
        }
    }
},{
    path: ':fruit_id/Sale', loadChildren: () => import('../Sale/Sale.module').then(m => m.SaleModule),
    data: {
        oPermission: {
            permissionId: 'Sale-detail-permissions'
        }
    }
},{
    path: ':fruit_id/SaleDetail', loadChildren: () => import('../SaleDetail/SaleDetail.module').then(m => m.SaleDetailModule),
    data: {
        oPermission: {
            permissionId: 'SaleDetail-detail-permissions'
        }
    }
},{
    path: ':fruit_id/SupplierFruit', loadChildren: () => import('../SupplierFruit/SupplierFruit.module').then(m => m.SupplierFruitModule),
    data: {
        oPermission: {
            permissionId: 'SupplierFruit-detail-permissions'
        }
    }
}
];

export const FRUIT_MODULE_DECLARATIONS = [
    FruitHomeComponent,
    FruitNewComponent,
    FruitDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class FruitRoutingModule { }