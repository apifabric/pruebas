import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SupplierFruitHomeComponent } from './home/SupplierFruit-home.component';
import { SupplierFruitNewComponent } from './new/SupplierFruit-new.component';
import { SupplierFruitDetailComponent } from './detail/SupplierFruit-detail.component';

const routes: Routes = [
  {path: '', component: SupplierFruitHomeComponent},
  { path: 'new', component: SupplierFruitNewComponent },
  { path: ':id', component: SupplierFruitDetailComponent,
    data: {
      oPermission: {
        permissionId: 'SupplierFruit-detail-permissions'
      }
    }
  }
];

export const SUPPLIERFRUIT_MODULE_DECLARATIONS = [
    SupplierFruitHomeComponent,
    SupplierFruitNewComponent,
    SupplierFruitDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SupplierFruitRoutingModule { }